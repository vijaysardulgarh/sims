import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import AffiliationForm
    from '../components/AffiliationForm';

const AffiliationCreatePage = () => {

    return (

        <CrudCreatePage
            title="Create Affiliation"
            endpoint="/compliance/affiliations/"
            FormComponent={AffiliationForm}
            redirectPath="/dashboard/compliance/affiliations"
        />

    );

};

export default AffiliationCreatePage;