import api from "./axios";

const getPermissions = async () => {

    const response =
        await api.get("permissions/");

    return response.data;
};

export default {
    getPermissions,
};