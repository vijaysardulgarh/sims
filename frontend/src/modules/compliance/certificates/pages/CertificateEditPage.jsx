import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import CertificateForm
    from '../components/CertificateForm';

const CertificateEditPage = () => {

    return (

        <CrudEditPage
            title="Edit Certificate"
            endpoint="/compliance/certificates/"
            FormComponent={CertificateForm}
            redirectPath="/dashboard/compliance/certificates"
        />

    );

};

export default CertificateEditPage;