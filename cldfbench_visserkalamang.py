import pathlib

import pylexibank
from idspy import IDSDataset, IDSEntry


class Dataset(IDSDataset):
    dir = pathlib.Path(__file__).parent
    id = "visserkalamang"
    writer_options = dict(keep_languages=False, keep_parameters=False)

    form_spec = pylexibank.FormSpec(missing_data=("∅",), replacements=[(" ", "_")])

    def cldf_specs(self):
        return super().cldf_specs()

    def cmd_download(self, args):
        self.raw_dir.xlsx2csv("ids_cl_Kalamang_EV_revised_BC.xlsx")

    def cmd_makecldf(self, args):
        glottocode = "kara1499"
        reprs = ["Phonemic"]

        args.writer.add_concepts(id_factory=lambda c: c.attributes["ids_id"])
        args.writer.add_sources(*self.raw_dir.read_bib())

        personnel = self.get_personnel(args)

        args.writer.add_language(
            ID=glottocode,
            Name="Kalamang",
            Glottocode=glottocode,
            Authors=personnel["author"],
            DataEntry=personnel["data entry"],
            Consultants=personnel["consultant"],
            Representations=reprs,
            date="2021-02-08",
        )

        for form in pylexibank.progressbar(
            self.read_csv("ids_cl_Kalamang_EV_revised_BC.Sheet1.csv")
        ):
            if form.form:
                is_loan = bool("loan" in form.comment)
                args.writer.add_lexemes(
                    Language_ID=glottocode,
                    Parameter_ID=form.ids_id,
                    Value=form.form,
                    Comment=form.comment,
                    Source="visser2021",
                    Transcriptions=reprs,
                    Loan=is_loan,
                )

        self.apply_cldf_defaults(args)
