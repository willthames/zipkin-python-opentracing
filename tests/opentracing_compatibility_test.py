import unittest

import opentracing
from opentracing.harness.api_check import APICompatibilityCheckMixin
from opentracing.mocktracer import MockTracer

import zipkin_ot.recorder
import zipkin_ot.tracer
from tests.recorder_test import MockConnection

class MockOpenzipkinTracer(MockTracer):
    def __init__(self):
        self.mock_connection = MockConnection()
        self.runtime_args = {'collector_host': 'localhost',
                             'collector_port': 9411,
                             'service_name': 'python/runtime_test',
                             'periodic_flush_seconds': 0,
                             'verbosity': 1}
        self.recorder = zipkin_ot.recorder.Recorder(**self.runtime_args)
        super(MockOpenzipkinTracer, self).__init__()

    def flush(self):
        self.recorder.flush()


class OpenzipkinTracerOpenTracingCompatibility(unittest.TestCase, APICompatibilityCheckMixin):
    def setUp(self):
        self._tracer = MockOpenzipkinTracer()

    def tracer(self):
        return self._tracer

    # from opentracing's tests.mocktracer.test_api.APICheckMockTracer
    def is_parent(self, parent, span):
        # use `Span` ids to check parenting
        if parent is None:
            return span.parent_id is None
        return parent.context.span_id == span.parent_id

    def tearDown(self):
        self._tracer.flush()


if __name__ == '__main__':
    unittest.main()
