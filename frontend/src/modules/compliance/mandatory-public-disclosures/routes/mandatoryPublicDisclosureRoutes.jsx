import { Route } from 'react-router-dom';

import MandatoryPublicDisclosuresListPage
    from '../pages/MandatoryPublicDisclosuresListPage';

import MandatoryPublicDisclosureCreatePage
    from '../pages/MandatoryPublicDisclosureCreatePage';

import MandatoryPublicDisclosureEditPage
    from '../pages/MandatoryPublicDisclosureEditPage';

const mandatoryPublicDisclosureRoutes = (

    <>

        <Route
            path="mandatory-public-disclosures"
            element={
                <MandatoryPublicDisclosuresListPage />
            }
        />

        <Route
            path="mandatory-public-disclosures/create"
            element={
                <MandatoryPublicDisclosureCreatePage />
            }
        />

        <Route
            path="mandatory-public-disclosures/edit/:id"
            element={
                <MandatoryPublicDisclosureEditPage />
            }
        />

    </>

);

export default mandatoryPublicDisclosureRoutes;