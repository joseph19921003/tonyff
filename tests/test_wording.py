from facefusion import wording


def test_get() -> None:
	assert wording.get('python_not_supported')
	assert wording.get('help.source')
	assert wording.get('invalid') is None
