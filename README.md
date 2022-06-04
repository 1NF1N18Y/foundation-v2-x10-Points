# Foundation Stratum Template (v2)

[![Foundation CI](https://github.com/blinkhash/foundation-server-v2/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/blinkhash/foundation-server-v2/actions/workflows/build.yml)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Discord](https://img.shields.io/discord/738590795384356904)](https://discord.gg/rNjez6VgNF)

This portal is a high performance Stratum server written entirely in Node.js. One instance of this software can startup and manage multiple coin pools, each with their own daemon and Stratum ports. This server itself was built to be efficient, transparent, and easy to setup, while still maintaining greater scalability than many of the other open-source Stratum servers. This repository itself, however, is simply a module. It will do nothing on its own. Unless you're a Node.js developer who would like to learn more regarding stratum authentication and raw share data, this module will not be of use to you. For a complete backend server that implements this module, see https://github.com/blinkhash/foundation-server-v2. It handles payments, database integration, multi-coin/pool support, and more.

#### Need Support?

If you need help with a code-related matter, the first place to look is our [Discord](https://discord.gg/rNjez6VgNF), where the developers will be available to answer any questions. However, please do not come to me with issues regarding setup. Use Google and the existing documentation for that.

---

### Donations

Maintaining this project has always been driven out of nothing more than a desire to give back to the mining community, however I always appreciate donations, especially if this repository helps you in any way.

- Bitcoin: 3EbrVYLxN5WeQmPpL6owo3A7rJELXecbbc
- Ethereum: 0xd3e3daED621d228244Fa89A3dd8AF07B52E72319
- Litecoin: MFWpARrSADAy3Qj79C4pSasS9F156QipwC
- ZCash: t1NSk8gyiou8TxWRZTVuUkfM5f9riopN58A

---

### License

Released under the GNU General Public License v3. See https://www.gnu.org/licenses/gpl-3.0 for more information

---