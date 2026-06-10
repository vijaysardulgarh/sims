import api from '../../../../services/api/axios';

const ENDPOINT =
    '/compliance/mandatory-public-disclosures/';

const mandatoryPublicDisclosureService = {

    getAll: () =>
        api.get(
            ENDPOINT
        ),

    getById: (id) =>
        api.get(
            `${ENDPOINT}${id}/`
        ),

    create: (data) =>
        api.post(
            ENDPOINT,
            data
        ),

    update: (
        id,
        data
    ) =>
        api.put(
            `${ENDPOINT}${id}/`,
            data
        ),

    delete: (id) =>
        api.delete(
            `${ENDPOINT}${id}/`
        ),

};

export default mandatoryPublicDisclosureService;