import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import ComplianceDocumentForm
    from '../components/ComplianceDocumentForm';

const ComplianceDocumentCreatePage = () => {

    return (

        <CrudCreatePage
            title="Create Compliance Document"
            endpoint="/compliance/compliance-documents/"
            FormComponent={ComplianceDocumentForm}
            redirectPath="/dashboard/compliance/compliance-documents"
        />

    );

};

export default ComplianceDocumentCreatePage;