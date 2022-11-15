from django.test import TestCase


class TestHidro(TestCase):
    def test_router_query_return_should_ok(self):
        self.asertTrue(True)

    def test_router_register_return_should_ok(self):
        self.asertTrue(True)
    
    def test_router_register_with_document_error_return_should_error(self):
        self.asertFalse(False)                

    def test_router_query_empty_return_should_ok(self):
        self.assertAlmostEqual([], [])