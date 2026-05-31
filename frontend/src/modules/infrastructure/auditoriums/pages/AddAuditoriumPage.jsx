import CrudCreatePage from '../../../../shared/components/common/crud/CrudCreatePage';

import AuditoriumForm from '../components/AuditoriumForm';

const AddAuditoriumPage = () => {

    return (
        <CrudCreatePage
            title="Add Auditorium"
            endpoint="/infrastructure/auditoriums/"
            FormComponent={AuditoriumForm}
            redirectPath="/dashboard/infrastructure/auditoriums"
        />
    );
};

export default AddAuditoriumPage;