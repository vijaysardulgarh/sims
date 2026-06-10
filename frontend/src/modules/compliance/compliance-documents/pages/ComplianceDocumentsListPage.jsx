import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

const ComplianceDocumentsListPage = () => {

    const columns = [

        {
            key: 'document_type',
            label: 'Document Type',
        },

        {
            key: 'title',
            label: 'Title',
        },

        {
            key: 'issuing_authority',
            label: 'Authority',
        },

        {
            key: 'expiry_date',
            label: 'Expiry Date',
        },

    ];

    return (

        <CrudListPage
            title="Compliance Documents"
            endpoint="/compliance/compliance-documents/"
            columns={columns}
            addPath="/dashboard/compliance/compliance-documents/create"
            editPath="/dashboard/compliance/compliance-documents/edit"
        />

    );

};

export default ComplianceDocumentsListPage;