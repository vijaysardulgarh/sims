import api from '../../../../services/api/axios';

const ENDPOINT =
    '/compliance/inspections/';

const inspectionService = {

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

export default inspectionService;