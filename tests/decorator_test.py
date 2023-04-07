def test_no_principal_decorator(client):
    response = client.get(
        '/student/assignments'
    )

    assert response.status_code == 401
    data = response.json

    assert data['error'] == 'FyleError'
    assert data['message'] == 'principal not found'


def test_requester_teacher(client, h_student_1):
    response = client.get(
        '/teacher/assignments',
        headers=h_student_1
    )
    assert response.status_code == 403
    data = response.json

    assert data['error'] == 'FyleError'
    assert data['message'] == 'requester should be a teacher'


def test_requester_student(client, h_teacher_1):
    response = client.get(
        '/student/assignments',
        headers=h_teacher_1
    )
    assert response.status_code == 403
    data = response.json

    assert data['error'] == 'FyleError'
    assert data['message'] == 'requester should be a student'


def test_wrong_api(client, h_teacher_1):
    response = client.get(
        '/trial',
        headers=h_teacher_1
    )

    assert response.status_code == 404
    data = response.json

    assert data['error'] == 'NotFound'
