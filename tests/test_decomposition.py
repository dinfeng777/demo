# tests/test_decomposition.py
from src.meta_agent.decomposition import decompose_project_description

def test_decompose_project_description_initial():
    # This test is part of demonstrating TDD.
    # We'd first make the function return this dummy list.
    # Then refactor the function and this test to expect an empty list.
    # For the subtask, we'll go straight to the final state for the function (empty list)
    # and the test will assert that.
    desc = "Develop a new web application."
    expected_tasks = [] # Final expected state
    assert decompose_project_description(desc) == expected_tasks

def test_decompose_empty_description():
    desc = ""
    expected_tasks = []
    assert decompose_project_description(desc) == expected_tasks

def test_decompose_with_keywords():
    # This is more of a conceptual test for a real feature
    desc = "Project with API and Database"
    # In a real scenario, we might expect keywords to influence output.
    # For placeholder, it still returns empty.
    expected_tasks = []
    assert decompose_project_description(desc) == expected_tasks
