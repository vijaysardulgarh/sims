import {
    useEffect,
    useState
} from "react";

import galleryService from "../services/galleryService";

const GalleriesListPage = () => {

    const [galleries, setGalleries] =
        useState([]);

    useEffect(() => {

        fetchGalleries();

    }, []);

    const fetchGalleries =
        async () => {

            const response =
                await galleryService
                    .getGalleries();

            setGalleries(
                response.data.results ||
                response.data
            );
        };

    return (

        <div>

            <h2>Galleries</h2>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>

                        <th>School</th>

                        <th>Title</th>

                        <th>Active</th>

                    </tr>

                </thead>

                <tbody>

                    {galleries.map(
                        (gallery) => (

                            <tr
                                key={gallery.id}
                            >

                                <td>
                                    {gallery.id}
                                </td>

                                <td>
                                    {
                                        gallery.school_name
                                    }
                                </td>

                                <td>
                                    {
                                        gallery.title
                                    }
                                </td>

                                <td>
                                    {
                                        gallery.is_active
                                            ? "Yes"
                                            : "No"
                                    }
                                </td>

                            </tr>
                        )
                    )}

                </tbody>

            </table>

        </div>
    );
};

export default GalleriesListPage;