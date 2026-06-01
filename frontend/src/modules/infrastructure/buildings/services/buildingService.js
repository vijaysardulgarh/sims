import api
from "../../../../services/api/axios";

const endpoint = "/buildings/";

export const getBuildings = () =>
    api.get(endpoint);

export const createBuilding = (data) =>
    api.post(endpoint, data);

export const updateBuilding = (
    id,
    data
) =>
    api.put(
        `${endpoint}${id}/`,
        data
    );

export const deleteBuilding = (id) =>
    api.delete(
        `${endpoint}${id}/`
    );