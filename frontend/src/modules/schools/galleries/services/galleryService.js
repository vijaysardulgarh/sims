import api from '../../../../services/api/axios';

const BASE_URL = '/schools/galleries/';

const galleryService = {

    getGalleries: async () =>
        await api.get(BASE_URL),

    getGallery: async (id) =>
        await api.get(`${BASE_URL}${id}/`),

    createGallery: async (data) =>
        await api.post(
            BASE_URL,
            data,
            {
                headers: {
                    "Content-Type":
                        "multipart/form-data",
                },
            }
        ),

    updateGallery: async (id, data) =>
        await api.put(
            `${BASE_URL}${id}/`,
            data,
            {
                headers: {
                    "Content-Type":
                        "multipart/form-data",
                },
            }
        ),

    deleteGallery: async (id) =>
        await api.delete(
            `${BASE_URL}${id}/`
        ),
};

export default galleryService;