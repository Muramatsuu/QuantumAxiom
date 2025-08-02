# test_quantumaxiom.py
"""
Tests for QuantumAxiom module.
"""

import unittest
from quantumaxiom import QuantumAxiom

class TestQuantumAxiom(unittest.TestCase):
    """Test cases for QuantumAxiom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumAxiom()
        self.assertIsInstance(instance, QuantumAxiom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumAxiom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
