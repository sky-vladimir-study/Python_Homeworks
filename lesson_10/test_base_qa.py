from CompanyTable import CompanyTable

db = CompanyTable("postgresql://postgres:2315@localhost:5432/QA")


def test_db_connection():
    names = db.base_connection()
    assert len(names) == 13


def test_select_group_student_list():
    lis = db.get_info_group_student()
    assert len(lis) == 676


def test_select_subject():
    inf = db.get_info_subject()
    assert len(inf) == db.count_from_subject()


def test_insert_subject():
    subject_id = 14
    subject_title = "Physics"
    count = db.count_from_subject()
    db.insert_into_subject(subject_id, subject_title)
    assert len(db.get_info_subject()) == count + 1

    db.delete_from_subject(subject_id)


def test_update_subject_title():
    subject_id = 19
    subject_title = "Alchemy"
    new_subject_title = "Chemistry"
    db.insert_into_subject(subject_id, subject_title)
    db.update_subject_title(new_subject_title, subject_id)
    body = db.get_info_subject_by_subject_id(subject_id)
    assert body[0]["subject_title"] == new_subject_title

    db.delete_from_subject(subject_id)


def test_delete_subject():
    subject_id = 145
    subject_title = "English"
    db.insert_into_subject(subject_id, subject_title)
    count = db.count_from_subject()
    db.delete_from_subject(subject_id)
    assert len(db.get_info_subject()) == count - 1
