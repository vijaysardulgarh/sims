import { useNavigate } from "react-router-dom";

import GalleryForm from "../components/GalleryForm";

import galleryService from "../services/galleryService";

const AddGalleryPage = () => {

    const navigate =
        useNavigate();

    const handleSubmit =
        async (data) => {

            await galleryService
                .createGallery(data);

            navigate(
                "/dashboard/schools/galleries"
            );
        };

    return (

        <GalleryForm
            onSubmit={handleSubmit}
        />
    );
};

export default AddGalleryPage;