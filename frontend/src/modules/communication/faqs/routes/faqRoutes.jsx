import { Route } from "react-router-dom";

import FAQsListPage
    from "../pages/FAQsListPage";

import AddFAQPage
    from "../pages/AddFAQPage";

import EditFAQPage
    from "../pages/EditFAQPage";

const faqRoutes = (

    <>
        <Route
            path="faqs"
            element={<FAQsListPage />}
        />

        <Route
            path="faqs/add"
            element={<AddFAQPage />}
        />

        <Route
            path="faqs/edit/:id"
            element={<EditFAQPage />}
        />
    </>

);

export default faqRoutes;