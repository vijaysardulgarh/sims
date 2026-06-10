// src/shared/admin/BaseAdminPage.jsx

import CrudListPage from "../components/crud/CrudListPage";

const BaseAdminPage = ({
    title,
    endpoint,
    columns,
}) => {

    return (
        <CrudListPage
            title={title}
            endpoint={endpoint}
            columns={columns}
        />
    );
};

export default BaseAdminPage;