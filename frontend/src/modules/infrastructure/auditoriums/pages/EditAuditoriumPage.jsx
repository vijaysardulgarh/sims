import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import AuditoriumForm from '../components/AuditoriumForm';

const EditAuditoriumPage = () => {

    return (
        <CrudEditPage
            title="Edit Auditorium"
            endpoint="/infrastructure/auditoriums/"
            FormComponent={AuditoriumForm}
            redirectPath="/dashboard/infrastructure/auditoriums"
        />
    );
};

export default EditAuditoriumPage;