// news/config/newsAdminConfig.js

const newsAdminConfig = {

    title: "News",

    endpoint:
        "/communications/news/",

    addPath:
        "/dashboard/communications/news/add",

    editPath:
        "/dashboard/communications/news/edit",

    columns: [

        {
            key: "title",
            label: "Title",
        },

        {
            key: "publish_date",
            label: "Publish Date",
        },

        {
            key: "is_published",
            label: "Published",
        },

    ],

};

export default newsAdminConfig;