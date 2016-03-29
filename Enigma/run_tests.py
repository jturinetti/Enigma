import unittest
from UnitTests import full_messages
from UnitTests import invalid_constructor_args
from UnitTests import invalid_method_args
from UnitTests import test_messages

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(full_messages.full_messages),
        loader.loadTestsFromTestCase(invalid_constructor_args.invalid_constructor_args),
        loader.loadTestsFromTestCase(invalid_method_args.invalid_method_args),
        loader.loadTestsFromTestCase(test_messages.test_messages)
    ))
    
    # TODO: make all tests pass
    
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite)