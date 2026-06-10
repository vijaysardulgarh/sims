import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import MandatoryPublicDisclosureForm
    from '../components/MandatoryPublicDisclosureForm';

const MandatoryPublicDisclosureEditPage = () => {

    return (

        <CrudEditPage
            title="Edit Mandatory Public Disclosure"
            endpoint="/compliance/mandatory-public-disclosures/"
            FormComponent={
                MandatoryPublicDisclosureForm
            }
            redirectPath="/dashboard/compliance/mandatory-public-disclosures"
        />

    );

};

export default MandatoryPublicDisclosureEditPage;