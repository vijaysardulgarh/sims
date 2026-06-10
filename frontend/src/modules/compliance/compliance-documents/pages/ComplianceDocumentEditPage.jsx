import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import ComplianceDocumentForm
    from '../components/ComplianceDocumentForm';

const ComplianceDocumentEditPage = () => {

    return (

        <CrudEditPage
            title="Edit Compliance Document"
            endpoint="/compliance/compliance-documents/"
            FormComponent={ComplianceDocumentForm}
            redirectPath="/dashboard/compliance/compliance-documents"
        />

    );

};

export default ComplianceDocumentEditPage;