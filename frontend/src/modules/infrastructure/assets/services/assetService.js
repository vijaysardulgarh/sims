import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/assets/';

export const getAssets = () =>
    api.get(endpoint);

export const getAsset = (id) =>
    api.get(`${endpoint}${id}/`);

export const createAsset = (
    data
) =>
    api.post(endpoint, data);

export const updateAsset = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteAsset = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );