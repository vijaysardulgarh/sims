import { Route } from 'react-router-dom';

import AffiliationsListPage
    from '../pages/AffiliationsListPage';

import AffiliationCreatePage
    from '../pages/AffiliationCreatePage';

import AffiliationEditPage
    from '../pages/AffiliationEditPage';

const affiliationRoutes = (

    <>

        <Route
            path="affiliations"
            element={
                <AffiliationsListPage />
            }
        />

        <Route
            path="affiliations/create"
            element={
                <AffiliationCreatePage />
            }
        />

        <Route
            path="affiliations/edit/:id"
            element={
                <AffiliationEditPage />
            }
        />

    </>

);

export default affiliationRoutes;