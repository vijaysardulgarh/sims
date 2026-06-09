import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import NoticeForm from '../components/NoticeForm';

const EditNoticePage = () => {

    return (
        <CrudEditPage
            title="Edit Notice"
            endpoint="/communications/notices/"
            FormComponent={NoticeForm}
            redirectPath="/dashboard/communications/notices"
        />
    );
};

export default EditNoticePage;