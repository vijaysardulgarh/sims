import CrudCreatePage from '../../../../shared/components/crud/CrudCreatePage';

import NoticeForm from '../components/NoticeForm';

const AddNoticePage = () => {

    return (
        <CrudCreatePage
            title="Add Notice"
            endpoint="/communications/notices/"
            FormComponent={NoticeForm}
            redirectPath="/dashboard/communications/notices"
        />
    );
};

export default AddNoticePage;