import { Route } from 'react-router-dom';

import CertificatesListPage
    from '../pages/CertificatesListPage';

import CertificateCreatePage
    from '../pages/CertificateCreatePage';

import CertificateEditPage
    from '../pages/CertificateEditPage';

const certificateRoutes = (

    <>

        <Route
            path="certificates"
            element={
                <CertificatesListPage />
            }
        />

        <Route
            path="certificates/create"
            element={
                <CertificateCreatePage />
            }
        />

        <Route
            path="certificates/edit/:id"
            element={
                <CertificateEditPage />
            }
        />

    </>

);

export default certificateRoutes;