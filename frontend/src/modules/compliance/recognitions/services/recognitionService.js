import api from '../../../../services/api/axios';

const ENDPOINT =
    '/compliance/recognitions/';

const recognitionService = {

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

export default recognitionService;