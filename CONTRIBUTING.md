# Contributing to Stream Scan

First off, thank you for considering contributing to Stream Scan! It's people like you that make Stream Scan such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, [make one](https://github.com/aka76bm/stream-scan/issues/new)! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

### Fork & create a branch

If this is something you think you can fix, then [fork Stream Scan](https://github.com/aka76bm/stream-scan/fork) and create a branch with a descriptive name.

A good branch name would be (where issue #38 is the ticket you're working on):

```sh
git checkout -b 38-add-awesome-new-feature
```

### Get the test suite running

Make sure you're running the test suite locally.

```sh
# After you've installed the dependencies
pytest
```

### Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first 😸

### Make a Pull Request

At this point, you should switch back to your main branch and make sure it's up to date with Stream Scan's main branch:

```sh
git remote add upstream https://github.com/aka76bm/stream-scan.git
git checkout main
git pull upstream main
```

Then update your feature branch from your local copy of main, and push it!

```sh
git checkout 38-add-awesome-new-feature
git rebase main
git push --set-upstream origin 38-add-awesome-new-feature
```

Finally, go to GitHub and [make a Pull Request](https://github.com/aka76bm/stream-scan/compare)

### Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing and merging, check out this guide on [merging vs. rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing).

## How to get in touch

If you need help, you can reach out to us at [INSERT CONTACT METHOD].

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
