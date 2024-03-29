from test.conftest import assert_frames_are_equal

from moto import mock_s3
from pandas import DataFrame

from tgedr.nihao.assorted.s3.s3_connector import S3Connector
from tgedr.nihao.impls.sinks.s3 import AwsPdDfParquetSink
from tgedr.nihao.impls.sources.s3 import AwsParquetPdDfSource


@mock_s3
def test_s3_sink_put(aws_credentials):
    df = DataFrame(
        {
            "symbol": {
                0: "XPTO",
            },
            "variable": {
                0: ("Adj Close", "AMZN"),
            },
            "value": {
                0: 0.09791699796915054,
            },
            "actual_time": {
                0: 863654400.0,
            },
        }
    )

    bucket = "thebucket"
    file_path = f"s3://{bucket}/thekey.parquet"

    s3 = S3Connector()
    s3._resource.create_bucket(Bucket=bucket)

    o = AwsPdDfParquetSink()
    o.put(obj=df, key=file_path)

    i = AwsParquetPdDfSource()
    actual = i.get(key=file_path)

    assert_frames_are_equal(actual, expected=df, sort_columns=[])
