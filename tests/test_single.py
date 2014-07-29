import json
from fixtures import PostResponder


def test_single_object():
    data = PostResponder.build({'id': 1, 'title': 'My title'})

    assert data == {'posts': [{'id': 1, 'title': 'My title'}]}


def test_multiple():
    data = PostResponder.build([
        {'id': 1, 'title': 'A title'},
        {'id': 2, 'title': 'Another title'},
    ])

    assert data == {
        'posts': [
            {'id': 1, 'title': 'A title'},
            {'id': 2, 'title': 'Another title'},
        ]
    }


def test_meta():
    data = PostResponder.build(
        {'id': 1, 'title': 'Yeah'},
        meta={'key': 'value'},
    )

    assert data['meta']['key'] == 'value'


def test_dumps():
    data = PostResponder.dumps([
        {'id': 1, 'title': 'A title'}
    ])

    assert json.loads(data) == {
        'posts': [
            {'id': 1, 'title': 'A title'}
        ]
    }