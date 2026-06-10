import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

const CertificatesListPage = () => {

    const columns = [

        {
            key: 'certificate_type',
            label: 'Type',
        },

        {
            key: 'certificate_number',
            label: 'Certificate No.',
        },

        {
            key: 'issuing_authority',
            label: 'Authority',
        },

        {
            key: 'status',
            label: 'Status',
        },

    ];

    return (

        <CrudListPage
            title="Certificates"
            endpoint="/compliance/certificates/"
            columns={columns}
            addPath="/dashboard/compliance/certificates/create"
            editPath="/dashboard/compliance/certificates/edit"
        />

    );

};

export default CertificatesListPage;