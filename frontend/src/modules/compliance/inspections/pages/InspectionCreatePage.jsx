import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import InspectionForm
    from '../components/InspectionForm';

const InspectionCreatePage = () => {

    return (

        <CrudCreatePage
            title="Create Inspection"
            endpoint="/compliance/inspections/"
            FormComponent={InspectionForm}
            redirectPath="/dashboard/compliance/inspections"
        />

    );

};

export default InspectionCreatePage;