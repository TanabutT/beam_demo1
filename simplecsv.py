import argparse

import apache_beam as beam
from apache_beam import Pipeline
from apache_beam.io import ReadFromText, WriteToText
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions


class transformcsv(beam.DoFn):
    def process(self, element):
        df = element.split(",")[:-1]
        yield ",".join(df)  # Join back with commas as a CSV string


def run(argv=None, save_main_session=True):
    with beam.Pipeline(options=PipelineOptions()) as p:
        df = p | ReadFromText(
            "./" + "input.csv"
        )  # reads each row of the file as an element and passes it to transform csv

        (
            df
            | beam.ParDo(transformcsv())
            | WriteToText(
                "./" + "output", file_name_suffix=".csv", shard_name_template=""
            )
        )


if __name__ == "__main__":
    run()
