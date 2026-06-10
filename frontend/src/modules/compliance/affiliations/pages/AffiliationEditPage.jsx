import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import AffiliationForm
    from '../components/AffiliationForm';

const AffiliationEditPage = () => {

    return (

        <CrudEditPage
            title="Edit Affiliation"
            endpoint="/compliance/affiliations/"
            FormComponent={AffiliationForm}
            redirectPath="/dashboard/compliance/affiliations"
        />

    );

};

export default AffiliationEditPage;