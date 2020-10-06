const postsPromise = fetch("https://api.dailysmarty.com/posts");
// console.log("Starting fetch call");
// console.log("After fetch call");
// console.log(postsPromise);
// console.log("After program has run");

postsPromise
  .then((data) => data.json())
  .then((data) => {
    data.posts.forEach((item) => {
      console.log(item.url_for_post);
    });
  })
  .catch((err) => {
    console.log(err);
  });

// // http is unsecure and returns a bad fetch call

// const postsPromise = fetch("http://api.dailysmarty.com/posts");

// postsPromise
//     .then(data => data.json())
//     .then(data => {
//         data.posts.forEach((item) => {
//           console.log(item.url_for_post);
//         });
//     })
// .catch((err) => {
//   console.log(err);
// });
