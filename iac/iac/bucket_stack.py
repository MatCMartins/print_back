from aws_cdk import (
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct


class BucketStack(Construct):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "BucketStack")

        self.course_bucket = s3.Bucket(
            self,
            "CourseBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
        )
        self.event_bucket = s3.Bucket(
            self,
            "EventBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
        )
        self.member_bucket = s3.Bucket(
            self,
            "MemberBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
        )
        self.student_org_bucket = s3.Bucket(
            self,
            "StudentOrganizationBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
        )
