import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import CertificateForm
    from '../components/CertificateForm';

const CertificateCreatePage = () => {

    return (

        <CrudCreatePage
            title="Create Certificate"
            endpoint="/compliance/certificates/"
            FormComponent={CertificateForm}
            redirectPath="/dashboard/compliance/certificates"
        />

    );

};

export default CertificateCreatePage;