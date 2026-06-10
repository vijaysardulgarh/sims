import { Route } from 'react-router-dom';

import ComplianceDocumentsListPage
    from '../pages/ComplianceDocumentsListPage';

import ComplianceDocumentCreatePage
    from '../pages/ComplianceDocumentCreatePage';

import ComplianceDocumentEditPage
    from '../pages/ComplianceDocumentEditPage';

const complianceDocumentRoutes = (

    <>

        <Route
            path="compliance-documents"
            element={
                <ComplianceDocumentsListPage />
            }
        />

        <Route
            path="compliance-documents/create"
            element={
                <ComplianceDocumentCreatePage />
            }
        />

        <Route
            path="compliance-documents/edit/:id"
            element={
                <ComplianceDocumentEditPage />
            }
        />

    </>

);

export default complianceDocumentRoutes;