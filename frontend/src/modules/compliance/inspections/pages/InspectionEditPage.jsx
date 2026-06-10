import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import InspectionForm
    from '../components/InspectionForm';

const InspectionEditPage = () => {

    return (

        <CrudEditPage
            title="Edit Inspection"
            endpoint="/compliance/inspections/"
            FormComponent={InspectionForm}
            redirectPath="/dashboard/compliance/inspections"
        />

    );

};

export default InspectionEditPage;