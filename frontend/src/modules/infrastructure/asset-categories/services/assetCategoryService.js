import api from '../../../../services/api/axios';

const endpoint =
    '/infrastructure/asset-categories/';

export const getAssetCategories = () =>
    api.get(endpoint);

export const getAssetCategory = (id) =>
    api.get(`${endpoint}${id}/`);

export const createAssetCategory = (
    data
) =>
    api.post(endpoint, data);

export const updateAssetCategory = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteAssetCategory = (
    id
) =>
    api.delete(
        `${endpoint}${id}/`
    );