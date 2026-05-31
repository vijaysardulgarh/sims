import {
    useEffect,
    useState
} from "react";

import {
    useNavigate,
    useParams
} from "react-router-dom";

import GalleryForm from "../components/GalleryForm";

import galleryService from "../services/galleryService";

const EditGalleryPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [gallery, setGallery] =
        useState(null);

    useEffect(() => {

        fetchGallery();

    }, [id]);

    const fetchGallery =
        async () => {

            const response =
                await galleryService
                    .getGallery(id);

            setGallery(
                response.data
            );
        };

    const handleSubmit =
        async (data) => {

            await galleryService
                .updateGallery(
                    id,
                    data
                );

            navigate(
                "/dashboard/schools/galleries"
            );
        };

    if (!gallery)
        return <p>Loading...</p>;

    return (

        <GalleryForm
            initialData={gallery}
            onSubmit={handleSubmit}
        />
    );
};

export default EditGalleryPage;