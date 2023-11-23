# omicshub: remap environment variables
import os
os.environ["MINIWDL__AWS__S3_UPLOAD_FOLDER"] = os.getenv("S3_BUCKET_MINIWDL", "") 

from .batch_job import BatchJob, BatchJobNoEFS  # noqa: F401
from .cli_run_s3upload import miniwdl_run_s3upload  # noqa: F401
from .cli_submit import miniwdl_submit_awsbatch  # noqa: F401
