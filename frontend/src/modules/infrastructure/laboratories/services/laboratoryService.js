import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/laboratories/';

export const getLaboratories = () =>
    api.get(endpoint);

export const getLaboratory = (id) =>
    api.get(`${endpoint}${id}/`);

export const createLaboratory = (
    data
) =>
    api.post(endpoint, data);

export const updateLaboratory = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteLaboratory = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );