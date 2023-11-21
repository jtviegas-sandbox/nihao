from moto import mock_s3
from pandas import DataFrame

from tgedr.nihao.commons.utils import assert_frames_are_equal
from tgedr.nihao.s3.s3_connector import S3Connector
from tgedr.nihao.sink.s3 import PdDataFrameS3Sink
from tgedr.nihao.source.s3 import PdDataFrameFromParquetSource


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

    o = PdDataFrameS3Sink(config={})
    o.put(obj=df, key=file_path)

    i = PdDataFrameFromParquetSource(config={})
    actual = i.get(key=file_path)

    assert_frames_are_equal(actual, expected=df, sort_columns=[])
