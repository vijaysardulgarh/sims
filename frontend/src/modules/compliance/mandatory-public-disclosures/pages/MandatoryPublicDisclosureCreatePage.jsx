import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import MandatoryPublicDisclosureForm
    from '../components/MandatoryPublicDisclosureForm';

const MandatoryPublicDisclosureCreatePage = () => {

    return (

        <CrudCreatePage
            title="Create Mandatory Public Disclosure"
            endpoint="/compliance/mandatory-public-disclosures/"
            FormComponent={
                MandatoryPublicDisclosureForm
            }
            redirectPath="/dashboard/compliance/mandatory-public-disclosures"
        />

    );

};

export default MandatoryPublicDisclosureCreatePage;